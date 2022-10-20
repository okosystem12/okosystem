import {newSocial} from "../../../../../../components/social/newSocial";
import {componentsData} from "../../../../componentsData";
import {makeAddEvent} from "../makeAddEvent";

export const newItem = () => {
    const {viewSearchAdd} = componentsData;
    viewSearchAdd.append(newSocial());
    makeAddEvent();
};