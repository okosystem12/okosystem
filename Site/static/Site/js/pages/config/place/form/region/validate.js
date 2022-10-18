import {componentsData} from "../../componentsData";
import {init as initHandler} from "../../../../../utils/form/init";
import {submit} from "./submit";

export const validate = () => {
    const regionNameLength = 2;
    const {regionForm} = componentsData;

    regionForm.validate({
        rules: {
            regionCountry: {
                required: true,
            },

            regionName: {
                required: true,
                minlength: regionNameLength,
                normalizer: $.trim
            },
        },
        messages: {
            regionCountry: {
                required: `Пожалуйста выберите название страны из представленного списска`,
            },
            regionName: {
                required: `Пожалуйста укажите название региона`,
                minlength: `Название региона должно содержать не менее ${regionNameLength} символов`
            },
        },
        ...initHandler,
        submitHandler: submit
    });
};