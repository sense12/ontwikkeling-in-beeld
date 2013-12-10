(function () {
    "use strict";

    var students = {
        "sumiko"   : {year: 3},
        "janara"   : {year: 3},
        "jenieke"  : {year: 3}
    };

    var studyYearProducts = {
        //year : [products]
        3: {"Proeve 2": 34}
    }

    var assignmentBundles = {
        // assignments bundle
        34: {
            title: "Proeve 2",
            milestones: {
                // assignments 
                1: {
                    title: "Omgaan met verschillen",
                    assignemnts: {
                        1: {
                            title: "presoonlijke visie",
                            weight: 1
                        },
                        2: {
                            title: "bedrijfs visie",
                            weight: 1
                        }
                        3: {
                            title: "verschillen overeenkomsten visie",
                            weight: 1
                        }
                    },
                    weight: 1
                },
                2: {
                    title: "activiteiten ontwikkelen",
                    assignemnts: {
                    },
                    weight: 1
                },
                3: {
                    title: "begeleiden en aansturen van de groep",
                    assignemnts: {
                    },
                    weight: 1
                }
            }
        }
    };




}());
