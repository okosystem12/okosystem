import {info} from "../../../../storage/config/place/info";
import {countriesList} from "../../../../storage/app/countriesList";
import {regionsList} from "../../../../storage/app/regionsList";
import {citiesList} from "../../../../storage/app/citiesList";

export const prepInfo = () => {
    info.clear();

    const regionPrefix = countriesList.value.length + 1000;
    const cityPrefix = regionPrefix + regionsList.value.length + 1000;

    countriesList.value.forEach((el, index) => {
        if (el.title !== '') {
            info.push({
                ...emptyRow,
                id: index,
                typeRow: 'country',
                realId: el.id,
                country: el.title
            });
        }
    });

    regionsList.value.forEach((el, index) => {
        const country = countriesList.value.find(elem => elem.id === el.country_id);
        if (el.title !== '' && country) {
            info.push({
                ...emptyRow,
                id: regionPrefix + index,
                typeRow: 'region',
                realId: el.id,
                country: country.title,
                country_id: country.id,
                region: el.title
            });
        }
    });

    citiesList.value.forEach((el, index) => {
        const country = countriesList.value.find(elem => elem.id === el.country_id);
        const region = regionsList.value.find(elem => elem.id === el.region_id);
        if (el.title !== '' && country) {
            info.push({
                ...emptyRow,
                id: cityPrefix + index,
                typeRow: 'city',
                realId: el.id,
                country: country.title,
                country_id: country.id,
                region: region?.title || '',
                region_id: region?.id || null,
                city: el.title
            });
        }
    })
};


const emptyRow = {
    id: '',
    country: '',
    region: '',
    city: ''
};
