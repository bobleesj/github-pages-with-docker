---
layout: page
title: Publications
permalink: /publications/
---
<style>
    a {
        
        text-decoration: none; /* Removes underline */
    }

    a:hover {
        
    }

    li {
        margin-bottom: 20px;
    }

</style>
<script>
const journalList = [
    {
        authors: "S. Lee, C. Chen, G. Garcia, A. O. Oliynyk",
        title: "Machine learning descriptors in materials chemistry used in multiple experimentally validated studies: Oliynyk elemental property dataset",
        journal: "Data in Brief",
        volume: "54",
        pages: "110178",
        year: "2024",
        doi: "https://doi.org/10.1016/j.dib.2024.110178",
        gscholar: "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=L07HlVsAAAAJ&citation_for_view=L07HlVsAAAAJ:IjCSPb-OGe4C",
        citations: "" // Add citation count if available
    },
    {
        authors: "K. P. McGuinness, A. O. Oliynyk, S. Lee, B. Molero-Sanchez, P. K. Addo",
        title: "Machine-learning prediction of thermal expansion coefficient for perovskite oxides with experimental validation",
        journal: "Physical Chemistry Chemical Physics",
        volume: "25",
        pages: "32123–32131",
        year: "2023",
        doi: "10.1039/D3CP04017H",
        gscholar: "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=L07HlVsAAAAJ&authuser=1&citation_for_view=L07HlVsAAAAJ:2osOgNQ5qMEC",
        citations: "" // Add citation count if available
    },
    {
        authors: "Y. Tyvanchuk, V. Babizhetskyy, S. Baran, A. Szytula, V. Smetana, S. Lee, A. O. Oliynyk, A. Mudring",
        title: "The crystal and electronic structure of RE<sub>23</sub>Co<sub>6.7</sub>In<sub>20.3</sub> (RE = Gd–Tm, Lu): A new structure type based on intergrowth of AlB<sub>2</sub>- and CsCl-type related slabs",
        journal: "Journal of Alloys and Compounds",
        volume: "976",
        pages: "173241",
        year: "2024",
        doi: "10.1016/j.jallcom.2023.173241",
        gscholar: "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=L07HlVsAAAAJ&authuser=1&citation_for_view=L07HlVsAAAAJ:qjMakFHDy7sC",
        citations: "" // Add citation count if available
    },
    {
        authors: "S. Lee, M. Patel, and R. Patel",
        title: "Electrospun nanofiber nerve guidance conduits for peripheral nerve regeneration: A review",
        journal: "European Polymer Journal",
        volume: "181",
        pages: "111663",
        year: "2022",
        doi: "10.1016/j.eurpolymj.2022.111663",
        gscholar: "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=L07HlVsAAAAJ&authuser=1&citation_for_view=L07HlVsAAAAJ:u5HHmVD_uO8C",
        citations: ""
    }
    // Add other entries in the same format if needed
];



const preprintList = [
    {
        authors: "S. Lee, C. Chen, G. Garcia, A. O. Oliynyk",
        title: "Machine learning descriptors in materials chemistry: prediction and experimental validation synthesis of novel intermetallic UCd<sub>3</sub>",
        year: "2023",
        doi: "10.26434/chemrxiv-2023-0nlzl",
        gscholar: "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=L07HlVsAAAAJ&citation_for_view=L07HlVsAAAAJ:UeHWp8X0CEIC",
        citations: "" // Add citation count if available
    }
]

const presentationList = [
    {
        authors: "S. Lee, N. K. Barua, A. O. Oliynyk",
        title: "High-throughput Crystal Structure Featurizer for Binary and Ternary Compounds",
        conference: "2024 Gordon Research Conference on Solid State Chemistry (July 2024)",
        type: "Poster",
        location: "New London, NH ",
        document: "",
        abstract: ""
    },
    {
        authors: "S. Lee, A. O. Oliynyk",
        title: "Machine-learned Features to Solve Crystal Structure Classification Problems",
        conference: "ACS Northeast Regional Meeting (NERM) 2022, Computational Tools for Materials Science",
        type: "Oral",
        location: "Rochester, NY",
        document: "2022-ACS-NERM-slides.pdf",
        abstract: "2022-ACS-NERM-abstract.pdf"
    },
    {
        authors: "S. Lee, S. L. Topper, R. Q. Topper",
        title: "TransRot: a Portable and Easy-to-Use Open Source Software Package for Simulated Annealing Monte Carlo Geometry Optimization of Nanoparticles",
        conference: "Molecular Quantum Mechanics (MQM) 2022",
        type: "Poster",
        location: "Blacksburg, VA",
        document: "2022-MQM-poster.pdf",
        abstract: "2022-MQM-abstract.pdf"
    },
    {
        authors: "S. Lee, R. Q. Topper, S. L. Topper",
        title: "Mag-Walking Simulated Annealing Monte Carlo Study of Nano-solvated Ammonium Chloride",
        conference: "ACS New York 69th Annual Undergraduate Research Symposium 2022",
        type: "Oral",
        location: "Virtual due to COVID-19",
        document: "2022-ACS-NY-URS-slides.pdf",
        abstract: "2022-ACS-NY-URS-abstract.pdf"
    }
];

const presentationContributedList = [
    
    {
        authors: "A. O. Oliynyk, S. Lee, N. K. Barua",
        title: "TiNiSi-type vs. ZrNiAl-type: One More Time with Interpretable ML and Experimental Validation",
        conference: "North American Solid State Chemistry Conference (NASSCC) 2023",
        type: "Poster",
        location: "Calgary, Canada",
        document: "2023-NASSCC-poster.pdf",
        abstract: ""
    },
    {
        authors: "A. O. Oliynyk, S. Lee, G. Garcia",
        title: "Machine learning descriptors in chemistry: prediction and experimental validation of UCd<sub>3</sub>",
        conference: "Solid-State Materials Chemistry and Data Science Hackathon (SSMCDAT)",
        type: "Oral",
        location: "Virtual",
        document: "",
        abstract: "",
        video: "https://www.youtube.com/watch?v=PsstodhuYPc"
    },
];

const bookChapterList = [
    {
        authors: "R. Q. Topper, S. L. Topper, and S. Lee",
        title: "TransRot: A Portable Software Package for Simulated Annealing Monte Carlo Geometry Optimization of Atomic and Molecular Clusters",
        year: "2023",
        editors: "T A. Hopkins, C A. Parish",
        publisher: "ACS Publications",
        volume: 1429,
        isbn13: 9780841297432,
        doi: "10.1021/bk-2022-1428.ch002",
        gscholar: "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=L07HlVsAAAAJ&authuser=1&citation_for_view=L07HlVsAAAAJ:d1gkVwhDpl0C",
        citations: "" // Add citation count if available
    }
]


function displayJournalList() {
    const container = document.getElementById('journalList');
    const ol = document.createElement('ol'); // Create an ordered list element
    container.appendChild(ol); // Append the ordered list to the container

    journalList.forEach((entry, index) => {
        const li = document.createElement('li'); // Create a list item
        li.classList.add('journal-entry'); // Add class for styling

        const formattedAuthors = entry.authors.replace('S. Lee', '<strong>S. Lee</strong>');
        const citationString = entry.citations ? ` (${entry.citations})` : ''; // Conditionally add citations

        li.innerHTML = `
            <strong>${entry.title}</strong> </br>
            ${formattedAuthors} </br>
            ${entry.journal}, ${entry.volume}, ${entry.pages} (${entry.year})</br> 
            <a href="https://doi.org/${entry.doi}">DOI</a> | <a href="${entry.gscholar}">Google Scholar</a> ${citationString}
        `;
        ol.appendChild(li); // Append the list item to the ordered list
    });
}

function displayPreprintList() {
    const container = document.getElementById('preprintList');
    const ol = document.createElement('ol'); // Create an ordered list element
    container.appendChild(ol); // Append the ordered list to the container

    preprintList.forEach((entry, index) => {
        const li = document.createElement('li'); // Create a list item
        li.classList.add('preprint-entry'); // Add class for styling

        // Assuming the entry object has title, authors, year, and doi properties
        const formattedAuthors = entry.authors.replace('S. Lee', '<strong>S. Lee</strong>');
        li.innerHTML = `
            <div><strong>${entry.title}</strong></div>
            <div>${formattedAuthors}</div>
            <div><a href="https://doi.org/${entry.doi}">ChemRxiv</a> | <a href="${entry.gscholar}">Google Scholar</a> </div>
        `;
        ol.appendChild(li); // Append the list item to the ordered list
    });
}


function displayPresentationList() {
    const container = document.getElementById('presentationList');
    const ol = document.createElement('ol'); // Create an ordered list element
    container.appendChild(ol); // Append the ordered list to the container

    presentationList.forEach((entry, index) => {
        const li = document.createElement('li'); // Create a list item
        li.classList.add('presentation-entry');

        let authorsFormatted = entry.authors.split(', ').map(author => {
            if (author === "S. Lee") {
                return `<strong>${author}</strong>`; // Bold "S. Lee"
            }
            return author;
        }).join(', ');
        // authorsFormatted = `<u>${authorsFormatted.split(', ')[0]}</u>${authorsFormatted.substring(authorsFormatted.indexOf(','))}`; // Underline the first author

        let links = '';
        if (entry.document) {
            links += `<a href="/files/presentation/${entry.document}">PDF</a>`;
        }
        if (entry.abstract) {
            if (links.length > 0) {
                links += ' | ';
            }
            links += `<a href="/files/presentation/${entry.abstract}">Abstract</a>`;
        }
        if (entry.video) {
            if (links.length > 0) {
                links += ' | ';
            }
            links += `<a href="${entry.video}" target="_blank">YouTube</a>`; // Add video link
        }

        li.innerHTML = `
            <div><strong>${entry.title}</strong></div>
            <div>${authorsFormatted}</div>
            ${entry.conference}. ${entry.type}. ${entry.location}
            ${links.length > 0 ? '<br>' + links : ''}
        `;
        ol.appendChild(li); // Append the list item to the ordered list
    });
}

function displayContributedPresentationList() {
    const container = document.getElementById('presentationContributedList');
    const ol = document.createElement('ol'); // Create an ordered list element
    container.appendChild(ol); // Append the ordered list to the container

    presentationContributedList.forEach((entry, index) => {
        const li = document.createElement('li'); // Create a list item
        li.classList.add('presentationContributed-entry');

        let authorsFormatted = entry.authors.split(', ').map(author => {
            if (author === "S. Lee") {
                return `<strong>${author}</strong>`; // Bold "S. Lee"
            }
            return author;
        }).join(', ');
        // authorsFormatted = `<u>${authorsFormatted.split(', ')[0]}</u>${authorsFormatted.substring(authorsFormatted.indexOf(','))}`; // Underline the first author

        let links = '';
        if (entry.document) {
            links += `<a href="/files/presentation/${entry.document}">PDF</a>`;
        }
        if (entry.abstract) {
            if (links.length > 0) {
                links += ' | ';
            }
            links += `<a href="/files/presentation/${entry.abstract}">Abstract</a>`;
        }
        if (entry.video) {
            if (links.length > 0) {
                links += ' | ';
            }
            links += `<a href="${entry.video}" target="_blank">YouTube</a>`; // Add video link
        }

        li.innerHTML = `
            <div><strong>${entry.title}</strong></div>
            <div>${authorsFormatted}</div>
            ${entry.conference}. ${entry.type}. ${entry.location}
            ${links.length > 0 ? '<br>' + links : ''}
        `;
        ol.appendChild(li); // Append the list item to the ordered list
    });
}





function displayBookChapterList() {
    const container = document.getElementById('bookChapter');
    const ol = document.createElement('ol'); // Create an ordered list element
    container.appendChild(ol); // Append the ordered list to the container

    bookChapterList.forEach((entry, index) => {
        const li = document.createElement('li'); // Create a list item
        li.classList.add('book-chapter-entry'); // Add class for styling

        // Assuming the entry object has properties like title, authors, bookTitle, editors, volume, pageRange, year, and doi
        const formattedAuthors = entry.authors.replace('S. Lee', '<strong>S. Lee</strong>');
        li.innerHTML = `
            <div><strong>${entry.title}</strong></div>
            <div>${formattedAuthors}, Eds: ${entry.editors}</div>
            <div>Physical Chemistry Research at Undergraduate Institutions: Innovative and Impactful Approaches, Volume 1, 2, 19-38</div>
            <div>ACS Publications (2022)</div>
            <div>ISBN13: ${entry.isbn13}</div>
            <div><a href="https://doi.org/${entry.doi}">DOI</a> | <a href="${entry.gscholar}">Google Scholar</a></div>
        `;
        ol.appendChild(li); // Append the list item to the ordered list
    });
}


window.onload = function() {
    displayJournalList();
    displayPresentationList();
    displayPreprintList();
    displayBookChapterList();
    displayContributedPresentationList();

    
};
</script>

### Journals
<div id="journalList"></div>

### Book chapter
<div id="bookChapter"></div>

### Preprint
<div id="preprintList"></div>

### Presentations
<div id="presentationList"></div>

### Contributed presentations
<div id="presentationContributedList"></div>
