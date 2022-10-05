import {vchList} from "../../../../../storage/app/vchList";
import {openForm} from "../../form/openForm";

export const edit = (id) =>
    openForm(vchList.value.find(el => el.id === id) || {});