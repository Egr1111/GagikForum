let col_items = document.querySelectorAll(".column-item");
let points_items = document.querySelectorAll(".item-point");

function requiredInput() {
  let requiredInputs = document.querySelectorAll("input[required]")
  console.log(requiredInputs)
  requiredInputs.forEach((element) => {
    document.styleSheets[0].insertRule(
      "label[for=" +
        element.id +
        "]::after {display: initial; color:red; content: '*'; font-size: 1.5em}",
      0
    );
  })
}

function columnItemsEvent() {
  points_items.forEach((element) => {
    element.addEventListener("click", () => {
      let item = element.parentElement.parentElement;
      let link = item.querySelector(".item");
      let items_in_item = [];
      let item_childers = Array.from(item.children);

      item_childers.forEach((child) => {
        if (child.classList.contains("column-item")) {
          items_in_item.push(child);
        }
      });

      element.classList.toggle("active");
      link.classList.toggle("active");

      items_in_item.forEach((item) => {
        item.classList.toggle("d-none");
      });
    });
  });
}

function checkColItems() {
  if (document.querySelector(".column-item-shell.open") != null) {
    let active_button = document.querySelector(
      ".column-item-shell.open"
    ).parentElement;
    let parent = active_button.parentElement;
    let point = active_button.querySelector(".item-point");
    if (point != null) {
      point.click();
    }
    while (parent.classList.contains("column-item")) {
      point = parent.querySelector(".item-point");
      if (point != null) {
        point.click();
      }
      parent = parent.parentElement;
      console.log(parent);
    }
  }
}

function addEvents() {
  columnItemsEvent();
}


function main() {
  try {
    addEvents();
    checkColItems();
    requiredInput()
  } catch (e) {
    alert("Error: " + e.name + ": " + e.message + ": " + e.stack);
  }
}

main();
