import {componentsData} from "../../componentsData";
import {setFormValue} from "./setFormValue";
import {editId} from "../../../../../storage/config/place/editId";
import {show} from "../../../../../utils/modal/show";

export const openForm = (data) =>
    show(
        componentsData.regionModal,
        () => setFormValue(data),
        () => {
            editId.clear();
            componentsData.regionForm.data('validator').resetForm();
        }
    );