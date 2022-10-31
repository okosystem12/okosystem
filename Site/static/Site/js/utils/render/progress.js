import {progressbar} from "../../components/progressbar";

export const progress = (data, type = 'display') =>
                type === 'display'
                    ? progressbar(data)
                    : data?.title;