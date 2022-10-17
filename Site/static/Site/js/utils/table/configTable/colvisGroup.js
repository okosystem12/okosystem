import {getPosList} from "../../list/getPosList";

export const colvisGroup = (table) => {

    const result = [];
    const alwaysPos = getPosList(table.columnsList.map(el => el.always), [true]);

    table.patternList.forEach(p => {
        const pList = table.patternColumnsList.filter(pc => pc.pattern_id === p.id);
        if (pList.length) {
            const showPos = [...getPosList(table.columnsList.map(el => el.id), pList.map(c => c.column_id)), ...alwaysPos];

            if (showPos.length) {
                result.push({
                    extend: 'colvisGroup',
                    text: p.name,
                    show: [...showPos],
                    hide: table.columnsList.map((el, index) => {
                        return index
                    }).filter(el => showPos.indexOf(el) === -1)
                })
            }
        }
    });

    if (result.length) {
        result.unshift('<h3>Шаблоны</h3>');
    }

    return result;
};