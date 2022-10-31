import {link} from "../../components/link";

export const linkList = (data = [], type = 'display') =>
                data?.map(el =>
                    type === 'display' ? link(el.link, el.value) : el.link
                ).join(type === 'display' ? '<br>' : ', ');