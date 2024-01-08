const observerTimeline = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      console.log(entry);
      if (entry.isIntersecting) {
        entry.target.classList.remove("hidden");
        entry.target.classList.add("timeline-a");
      }
      // else{
      // 	// entry.target.classList.add('hidden');
      // 	entry.target.classList.remove('timeline-a');
      // }
    });
  });
  const observerContainer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      console.log(entry);
      if (entry.isIntersecting) {
        entry.target.classList.remove("hidden-a");
        entry.target.classList.add("container-a");
      }
      // else{
      // 	// entry.target.classList.add('hidden');
      // 	entry.target.classList.remove('timeline-a');
      // }
    });
  });
  // const observerAll = new IntersectionObserver((entries) => {
  //   entries.forEach((entry) => {
  //     console.log(entry);
  //     if (entry.isIntersecting) {
  //       entry.target.classList.remove("hidden-all");
  //       entry.target.classList.add("show");
  //     }
  //     // else{
  //     // 	// entry.target.classList.add('hidden');
  //     // 	entry.target.classList.remove('timeline-a');
  //     // }
  //   });
  // });

  const observer= new IntersectionObserver((entries) => {
    entries.forEach((entry)=>{
        console.log(entry);
        if(entry.isIntersecting){
            entry.target.classList.add('show');
        }
        // else{
        //     entry.target.classList.remove('show');
        // }
    });
}
);


const hiddenElements = document.querySelectorAll(".hidden");
hiddenElements.forEach((el) => observerTimeline.observe(el));
const hiddenContainer = document.querySelectorAll(".hidden-a");
hiddenContainer.forEach((el) => observerContainer.observe(el));
const hiddenAll = document.querySelectorAll('.hidden-all');
hiddenAll.forEach((el)=> observer.observe(el));
// const hiddenAll = document.querySelectorAll(".hidden-all");
  // hiddenAll.forEach((el) => observerAll.observe(el));