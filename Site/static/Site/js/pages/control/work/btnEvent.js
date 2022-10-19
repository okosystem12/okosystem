import {btnAddEvent} from "../form/btnAddEvent";
import {btnViewSearchEvent} from "../view/btn/btnViewSearchEvent";
import {btnViewAnalysisEvent} from "../view/btn/btnViewAnalysisEvent";
import {btnViewArchiveEvent} from "../view/btn/btnViewArchiveEvent";
import {viewSearchAddBtn} from "../view/btn/viewSearchAddBtn";

export const btnEvent = () =>{
    btnAddEvent();
    btnViewSearchEvent();
    btnViewAnalysisEvent();
    btnViewArchiveEvent();
    viewSearchAddBtn();
};