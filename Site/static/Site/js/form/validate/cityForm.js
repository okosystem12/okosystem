import {componentsData} from "../../pages/config/place/componentsData";
import {init as initHandler} from "./handler/init";
import {cityForm as submitForm} from "../submit/cityForm";

export const cityForm = () => {
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
        submitHandler: submitForm
    });
};