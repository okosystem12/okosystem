import {componentsData} from "../componentsData";
import {openForm} from "../form/region/openForm";

export const regionBtnAddEvent = () =>
    componentsData.regionBtnAdd.on('click', () => {
        openForm()
    });