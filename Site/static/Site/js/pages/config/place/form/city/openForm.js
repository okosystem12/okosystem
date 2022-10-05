import {componentsData} from "../../componentsData";
import {fancybox} from "../../../../../utils/fancybox";
import {setFormValue} from "./setFormValue";
import {editId} from "../../../../../storage/config/place/editId";
import {show} from "../../../../../utils/modal/show";

export const openForm = (data) =>
    show(
        componentsData.cityModal,
        () => setFormValue(data),
        () => {
            editId.clear();
            componentsData.cityForm.data('validator').resetForm();
        }
    );