import {componentsData} from "../componentsData";
import {type} from "../../../../storage/config/place/type";

export const btnToggleByType = () => {
    const {countryBtnAdd, regionBtnAdd, cityBtnAdd} = componentsData;

    countryBtnAdd.hide();
    regionBtnAdd.hide();
    cityBtnAdd.hide();

    switch (type.value) {
        case 'countries':
            countryBtnAdd.show();
            break;
        case 'regions':
            countryBtnAdd.show();
            regionBtnAdd.show();
            break;
        default:
            countryBtnAdd.show();
            regionBtnAdd.show();
            cityBtnAdd.show();
            break;

    }
};