import {componentsData} from "../componentsData";
import {setFormValue} from "./setFormValue";
import {userId} from "../../../storage/control/userId";
import {show} from "../../../utils/modal/show";

export const openForm = (data = {}) =>
    show(
        componentsData.controlModal,
        () => setFormValue(data),
        () => {
            userId.clear();
            componentsData.controlForm.data('validator').resetForm();
        }
    );