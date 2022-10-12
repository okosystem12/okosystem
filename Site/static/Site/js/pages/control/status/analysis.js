import {analysis as startAnalysis} from "../../../req/control/status/analysis";
import {userId} from "../../../storage/control/userId";
import {close} from "../view/close";

export const analysis = () =>
    startAnalysis({id: userId.value}, close);