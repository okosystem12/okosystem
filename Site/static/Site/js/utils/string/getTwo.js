export const getTwo = (value) => {
  return value < 10 ? '0' + value : value % 100;
};