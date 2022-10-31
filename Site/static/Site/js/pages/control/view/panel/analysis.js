import {componentsData} from "../../componentsData";
import {loader} from "../../../../components/loader";
import {corruptList} from "../../../../storage/control/corruptList";
import {fillAnalysis} from "./analysis/fillAnalysis";

export const analysis = (data = null) => {
    const {viewAnalysis} = componentsData;
    viewAnalysis.html('');

    switch (data?.status.stage) {
        case 'prepare':
            viewAnalysis.html('<p class="lead text-center">Список пуст</p>');
            break;
        case 'work':
            if (corruptList.value.length === 0) {
                switch (data?.status.type) {
                    case 'init':
                        viewAnalysis.html('<p class="lead text-center">Список пуст</p>');
                        break;
                    case 'analysis':
                        viewAnalysis.html(loader('Ожидайте завершения анализа'));
                        break;
                    case 'warning':
                        break;
                    case 'success':
                        viewAnalysis.html('<p class="lead text-center">Нарушений не выявлено</p>');
                        break;
                }
            } else {
                fillAnalysis(data);
            }
            break;
    }
};