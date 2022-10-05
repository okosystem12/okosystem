import {componentsData} from "../componentsData";
import {openForm} from "../form/country/openForm";


export const countryBtnAddEvent = () =>
    componentsData.countryBtnAdd.on('click', () => {
        openForm()
    });