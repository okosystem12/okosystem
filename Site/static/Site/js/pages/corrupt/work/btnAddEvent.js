import {componentsData} from "../componentsData";
import {openForm} from "../form/openForm";

export const btnAddEvent = () =>
    componentsData.corruptBtnAdd.on('click', () => {
        openForm()
    });