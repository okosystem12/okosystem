import {componentsData} from "../../vch/componentsData";
import {openForm} from "../../vch/form/openForm";

export const vchBtnAddEvent = () =>
    componentsData.vchBtnAdd.on('click', () => {
        openForm()
    });