import {newSocial} from "../../../../../../components/social/newSocial";
import {componentsData} from "../../../../componentsData";
import {makeAddEvent} from "../makeAddEvent";

export const newItem = () => {
    const {viewSearch} = componentsData;
    viewSearch.append(newSocial());
    makeAddEvent();
};