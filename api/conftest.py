import pytest
import logging

log = logging.getLogger(__name__)

# Contadores para métricas do pytest-html
test_metrics = {
    "expected_failures": 0,
    "unexpected_passes": 0, 
    "errors": 0,
    "reruns": 0
}

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Adiciona sumário completo ao final da execução."""
    
    # Coleta estatísticas
    stats = terminalreporter.stats
    passed = len(stats.get('passed', []))
    failed = len(stats.get('failed', []))
    skipped = len(stats.get('skipped', []))
    
    # Formata igual ao pytest-html
    summary_line = f"{failed} Failed,{passed} Passed,{skipped} Skipped,{test_metrics['expected_failures']} Expected failures,{test_metrics['unexpected_passes']} Unexpected passes,{test_metrics['errors']} Errors,{test_metrics['reruns']} Reruns"
    
    # Log do sumário
    print("\n" + "="*60)
    print("📊 SUMÁRIO DE TESTES")
    print("="*60)
    print(f"📋 {summary_line}")
    print("="*60)

# Hook para detectar expected failures
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if hasattr(report, 'wasxfail') and report.when == "call":
        if report.passed:
            test_metrics["unexpected_passes"] += 1
        else:
            test_metrics["expected_failures"] += 1
    
    if report.when in ('setup', 'teardown') and report.failed:
        test_metrics["errors"] += 1

# Adicionar no final do conftest.py existente:

# Hooks para capturar reruns
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item, nextitem):
    """Captura reruns de testes."""
    reports = yield
    # Conta reruns se o teste foi executado múltiplas vezes
    if hasattr(item, 'execution_count') and item.execution_count > 1:
        test_metrics["reruns"] += item.execution_count - 1

# Hooks para pytest-html integração completa
@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    """Atualiza o sumário do pytest-html com as métricas capturadas."""
    # Remove zeros e adiciona apenas métricas com valores
    metrics = []
    if test_metrics['expected_failures'] > 0:
        metrics.append(f"{test_metrics['expected_failures']} Expected failures")
    if test_metrics['unexpected_passes'] > 0:
        metrics.append(f"{test_metrics['unexpected_passes']} Unexpected passes")
    if test_metrics['errors'] > 0:
        metrics.append(f"{test_metrics['errors']} Errors")
    if test_metrics['reruns'] > 0:
        metrics.append(f"{test_metrics['reruns']} Reruns")
    
    # Adiciona ao sumário
    for metric in metrics:
        summary.append(metric)

# Hook para capturar erros de setup/teardown mais precisamente
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup(item):
    try:
        yield
    except Exception:
        test_metrics["errors"] += 1
        raise

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item, nextitem):
    try:
        yield
    except Exception:
        test_metrics["errors"] += 1
        raise

def test_com_erro_setup():
    # Erro no setup ou teardown incrementará Errors
    raise Exception("Erro durante execução")

@pytest.mark.xfail(reason="Esperado falhar, mas passou!")
def test_nao_deveria_passar():
    assert True  # Isso incrementará Unexpected passes

def test_com_erro_setup():
    # Erro no setup ou teardown incrementará Errors
    raise Exception("Erro durante execução")

