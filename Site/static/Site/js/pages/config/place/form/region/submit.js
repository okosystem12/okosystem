import {componentsData} from "../../componentsData";
import {work} from "../../../../../req/config/place/regions/work";
import {editId} from "../../../../../storage/config/place/editId";
import {highlight} from "../../../../../utils/form/highlight";
import {close} from "./close";
import {placeInfo} from "../../../../app/placeInfo";

export const submit = (form, e) => {
    e.preventDefault();
    const {regionName, regionCountry, regionModal} = componentsData;

    work({
        id: editId.value,
        country_id: regionCountry.val(),
        title: regionName.val().trim(),
    }, (msg) => {
        if (msg.successText) {
            close();
            placeInfo();
        }
        else {
            highlight(regionName, msg.errorHighlight);
        }
    });
};