import {componentsData} from "../componentsData";
import {emptyControlForm} from "./emptyControlForm";
import {openForm} from "./openForm";
import {userId} from "../../../storage/control/userId";

export const btnAddEvent = () =>
    componentsData.controlBtnAdd.on('click', () => openForm(emptyControlForm));