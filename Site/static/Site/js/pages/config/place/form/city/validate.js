import {componentsData} from "../../componentsData";
import {init as initHandler} from "../../../../../utils/form/init";
import {submit} from "./submit";

export const validate = () => {
    const cityNameLength = 2;
    const {cityForm} = componentsData;

    cityForm.validate({
        rules: {
            cityCountry: {
                required: true,
            },

            cityName: {
                required: true,
                minlength: cityNameLength,
                normalizer: $.trim
            },
        },
        messages: {
            cityCountry: {
                required: `Пожалуйста выберите название страны из представленного списска`,
            },
            cityName: {
                required: `Пожалуйста укажите название города`,
                minlength: `Название города должно содержать не менее ${cityNameLength} символов`
            },
        },
        ...initHandler,
        submitHandler: submit
    });
};