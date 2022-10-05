import {componentsData} from "../../pages/config/place/componentsData";
import {highlight} from "../validate/handler/highlight";
import {work} from "../../req/config/place/contries/work";
import {editId} from "../../storage/config/place/editId";
import {placeInfo} from "../../pages/app/placeInfo";
import {hide} from "../../utils/modal/hide";

export const countryForm = (form, e) => {
    e.preventDefault();
    const {countryName, countryModal} = componentsData;

    work({
        id: editId.value,
        title: countryName.val().trim(),
    }, (msg) => {
        if (msg.successText) {
            hide(countryModal);
            placeInfo();
        }
        else {
            highlight(countryName);
        }
    });
};