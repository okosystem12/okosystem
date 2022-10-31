import {componentsData} from "../../componentsData";
import {loader} from "../../../../components/loader";
import {fillSearchSocial} from "./search/fillSearchSocial";
import {socialList} from "../../../../storage/control/socialList";


export const search = (data = {}) => {
    const {viewSearch, viewSearchAdd} = componentsData;

    viewSearch.html('');
    viewSearchAdd.html('');

    switch (data?.status.stage) {
        case 'prepare':
            if (socialList.value.length === 0) {
                switch (data?.status.type) {
                    case 'init':
                        viewSearch.html('<p class="lead text-center">Список пуст</p>');
                        break;
                    case 'search':
                        viewSearch.html(loader('Ожидайте завершения поиска'));
                        break;
                    case 'equal':
                        break;
                    case 'notEqual':
                        viewSearch.html('<p class="lead text-center">Совпадений не выявлено</p>');
                        break;
                }
            } else {
                fillSearchSocial(data);
            }
            break;
        case 'work':
            fillSearchSocial(data);
            break;
    }

};