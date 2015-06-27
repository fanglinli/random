// Event listener for sorting button
var button = document.getElementById("sort-button");
var buttonSortFn = function() {sortByClass(".posts", ".post", ".timestamp")};

if (document.addEventListener) {
    button.addEventListener("click", buttonSortFn);
} else { // Fallback for IE...
    button.attachEvent("onclick", buttonSortFn);
}

// Sorts elements with class targetClass by its inner element with class sortingClass
function sortByClass(parentClass, targetClass, sortingClass) {
    // Store target elements in a list
    var posts = document.querySelectorAll(targetClass);
    var postList = [];
    for (var i = 0; i < posts.length; ++i) {
        postList[i] = posts[i];
    }

    // Sort (increasing order)
    postList.sort(function (a, b) {
        return a.querySelector(sortingClass).innerText -
                b.querySelector(sortingClass).innerText;
    });

    // Append sorted elements to parent container
    var parentElement = document.querySelector(parentClass);
    for (i = 0; i < postList.length; ++i) {
        parentElement.appendChild(postList[i]);
    }
}
