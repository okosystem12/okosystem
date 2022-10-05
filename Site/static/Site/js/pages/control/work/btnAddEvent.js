import {componentsData} from "../componentsData";
import {emptyControlForm} from "../form/emptyControlForm";
import {openForm} from "../form/openForm";
import {userId} from "../../../storage/control/userId";

export const btnAddEvent = () =>
    componentsData.controlBtnAdd.on('click', () => openForm(emptyControlForm));