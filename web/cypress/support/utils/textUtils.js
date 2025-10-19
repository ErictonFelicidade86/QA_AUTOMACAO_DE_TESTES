export const normalizeText = (text) => {
  return text
    .normalize('NFC')
    .replace(/\u00a0/g, ' ')
    .replace(/\u200b/g, '')
    .replace(/\s+/g, ' ')
    .trim();
};
