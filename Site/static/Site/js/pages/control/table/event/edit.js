import {userId} from "../../../../storage/control/userId";
import {openForm} from "../../form/openForm";
import {controlUserList} from "../../../../storage/control/controlUserList";

export const edit = (id) => {
    userId.value = parseInt(id);
    openForm(controlUserList.value.find(user => user.id === userId.value));
};