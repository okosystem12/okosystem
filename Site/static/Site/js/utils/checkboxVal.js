export const checkboxVal = (elem, value) => {
  if (value === undefined) {
    return elem.prop('checked');
  }
  else {
    elem.prop('checked', !!value);
  }
};