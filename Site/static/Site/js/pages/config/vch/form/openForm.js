import {componentsData} from "../componentsData";
import {show} from "../../../../utils/modal/show";
import {setFormValue} from "./setFormValue";
import {editId} from "../../../../storage/config/vch/editId";

export const openForm = (data) =>
    show(
        componentsData.vchModal,
        () => setFormValue(data),
        ()=> {
            editId.clear();
            componentsData.vchForm.data('validator').resetForm();
        }
    );