import {componentsData} from "../../componentsData";
import {highlight} from "../../../../../utils/form/highlight";
import {work} from "../../../../../req/config/place/countries/work";
import {editId} from "../../../../../storage/config/place/editId";
import {close} from "./close";
import {placeInfo} from "../../../../app/placeInfo";

export const submit = (form, e) => {
    e.preventDefault();
    const {countryName} = componentsData;

    work({
        id: editId.value,
        title: countryName.val().trim(),
    }, (msg) => {
        if (msg.successText) {
            close();
            placeInfo();
        }
        else {
            highlight(countryName, msg.errorHighlight);
        }
    });
};