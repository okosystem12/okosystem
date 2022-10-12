export const progress = (data = {}) =>
    `<div class="progress">
<div class="progress__bar progress__bar_type_${data.state}" style="width: ${data.value}%" title="${data.value}%"></div>
</div>`;