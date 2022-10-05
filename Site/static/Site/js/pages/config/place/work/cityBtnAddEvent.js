import {componentsData} from "../componentsData";
import {openForm} from "../form/city/openForm";

export const cityBtnAddEvent = () =>
    componentsData.cityBtnAdd.on('click', () => {
        openForm()
    });