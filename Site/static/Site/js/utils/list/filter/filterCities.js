import {citiesList} from "../../../storage/app/citiesList";

export const filterCities = (country = null, region = null) =>
    citiesList.value.filter(el =>
        (country ? el.country_id === country : true)
        &&
        (region ? el.region_id === region : true)
    );