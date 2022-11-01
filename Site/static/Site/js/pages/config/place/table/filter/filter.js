import {def} from "../../../../../utils/table/filter/def";

export const filter = (table) => [
    def(table, 'Страны', 'type', {value: 'countries', title: 'Отображать только', text: 'Страны'}),
    def(table, 'Страны и регионы', 'type', {value: 'regions', title: 'Отображать только', text: 'Страны и регионы'})
];