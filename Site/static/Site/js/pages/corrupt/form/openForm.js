import {componentsData} from "../componentsData";
import {show} from "../../../utils/modal/show";
import {setFormValue} from "./setFormValue";
import {editId} from "../../../storage/corrupt/editId";

export const openForm = (data) =>
    show(
        componentsData.corruptModal,
        () => setFormValue(data),
        ()=> {
            editId.clear();
            componentsData.corruptForm.data('validator').resetForm();
        }
    );