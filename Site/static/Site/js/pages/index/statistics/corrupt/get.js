import {corrupt} from "../../../../req/index/statistics/corrupt";
import {fill} from './fill'

export const get = () =>
    corrupt((msg) =>
        fill(msg.corruptList));