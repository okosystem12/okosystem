import {componentsData} from "../../componentsData";
import {highlight} from "../../../../../utils/form/highlight";
import {work} from "../../../../../req/config/place/contries/work";
import {editId} from "../../../../../storage/config/place/editId";
import {placeInfo} from "../../../../app/placeInfo";
import {hide} from "../../../../../utils/modal/hide";

export const submit = (form, e) => {
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