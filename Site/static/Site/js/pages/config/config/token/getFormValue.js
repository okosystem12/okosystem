import {get} from "../../../../req/config/token/get";
import {setFormValue} from "./setFormValue";

export const getFormValue = () =>
    get(setFormValue);