import {row as statisticsRow} from "../../../components/statistics/row";
import {elem as statisticsElem} from "../../../components/statistics/elem";

export const filHelper = (place = null, statisticsList = []) =>
    statisticsList.forEach(el => {
        if (place) {
            if (el.subList) {
                place.append(statisticsRow(el));
                filHelper(place, el.subList);
            }
            else {
                place.append(statisticsElem(el));
            }
        }
    });
