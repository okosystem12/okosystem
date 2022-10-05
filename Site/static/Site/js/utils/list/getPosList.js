export const getPosList = (list, valueList) =>{
    const result = [];

    valueList.forEach((el) => {
        result.push(list.indexOf(el))
    });

    return result.filter(el => el !== -1);
};