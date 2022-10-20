import {componentsData} from "../../componentsData";
import {loader} from "../../../../components/loader";
import {fillSearchSocial} from "./search/fillSearchSocial";


export const search = (data = {}) => {
    const {viewSearch, viewSearchAdd} = componentsData;

    viewSearch.html('');
    viewSearchAdd.html('');

    switch (data?.status.stage) {
        case 'prepare':
            switch (data?.status.type) {
                case 'init':
                    viewSearch.html('<p class="lead text-center">Запустите поиск сотрудника</p>');
                    break;
                case 'search':
                    viewSearch.html(loader('Ожидайте завершения поиска'));
                    break;
                case 'equal':
                    fillSearchSocial();
                    break;
                case 'notEqual':
                    viewSearch.html('<p class="lead text-center">Совпадений не выявлено</p>');
                    break;
            }
            break;
        case 'work':
            fillSearchSocial();
            break;
    }

};