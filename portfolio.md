---
layout: page
title: Publications
permalink: /publications/
---
<style>
    a {
    color: #007bff; /* Example color */
    text-decoration: none; /* Removes underline */
    /* Other styles */
}

    a:hover {
        color: #0056b3; /* Example hover color */
        text-decoration: underline; /* Adds underline on hover */
}

</style>
<script>
const journalList = [
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
        title: "The crystal and electronic structure of RE23Co6.7In20.3 (RE = Gd–Tm, Lu): A new structure type based on intergrowth of AlB2- and CsCl-type related slabs",
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

const presentationList = [
    {
        authors: "A. O. Oliynyk, S. Lee, N. K. Barua",
        title: "TiNiSi-type vs. ZrNiAl-type: One More Time with Interpretable ML and Experimental Validation",
        conference: "North American Solid State Chemistry Conference (NASSCC) 2023",
        type: "Poster",
        location: "Calgary, Canada",
        date: "August 2023",
        document: "2023-NASSCC-poster.pdf",
        abstract: ""
    },
    {
        authors: "S. Lee, A. O. Oliynyk",
        title: "Machine-learned Features to Solve Crystal Structure Classification Problems",
        conference: "ACS Northeast Regional Meeting (NERM) 2022, Computational Tools for Materials Science",
        type: "Oral",
        location: "Rochester, NY",
        date: "October 2022",
        document: "2022-ACS-NERM-slides.pdf",
        abstract: "2022-ACS-NERM-abstract.pdf"
    },
    {
        authors: "S. Lee, S. L. Topper, R. Q. Topper",
        title: "TransRot: a Portable and Easy-to-Use Open Source Software Package for Simulated Annealing Monte Carlo Geometry Optimization of Nanoparticles",
        conference: "Molecular Quantum Mechanics (MQM) 2022",
        type: "Poster",
        location: "Blacksburg, VA",
        date: "June 2022",
        document: "2022-MQM-poster.pdf",
        abstract: "2022-MQM-abstract.pdf"
    },
    {
        authors: "S. Lee, R. Q. Topper, S. L. Topper",
        title: "Mag-Walking Simulated Annealing Monte Carlo Study of Nano-solvated Ammonium Chloride",
        conference: "ACS New York 69th Annual Undergraduate Research Symposium 2022",
        type: "Oral",
        location: "Virtual due to COVID-19",
        date: "May 2022",
        document: "2022-ACS-NY-URS-slides.pdf",
        abstract: "2022-ACS-NY-URS-abstract.pdf"
    }
];



function displayJournalList() {
    const container = document.getElementById('journalList');
    const totalEntries = journalList.length;
    journalList.forEach((entry, index) => {
        const div = document.createElement('div');
        div.classList.add('journal-entry'); // Add class for styling
        const formattedAuthors = entry.authors.replace('S. Lee', '<strong>S. Lee</strong>');
        const citationString = entry.citations ? ` (${entry.citations})` : ''; // Conditionally add citations
        const number = totalEntries - index; // Calculate reverse order number
        div.innerHTML = `
            <p>
            ${number}. ${formattedAuthors}, "${entry.title}." <em>${entry.journal}</em>, <strong>${entry.volume}</strong>, ${entry.pages} (${entry.year}).</br> 
            <a href="https://doi.org/${entry.doi}">DOI</a> | <a href="${entry.gscholar}">Google Scholar</a> ${citationString}
            </p>
            `;
        container.appendChild(div);
    });
}


function displayPresentationList() {
    const container = document.getElementById('presentationList');
    presentationList.forEach((entry, index) => {
        const div = document.createElement('div');
        div.classList.add('presentation-entry');

        let authorsFormatted = entry.authors.split(', ').map(author => {
            if (author === "S. Lee") {
                return `<strong>${author}</strong>`; // Bold "S. Lee"
            }
            return author;
        }).join(', ');
        authorsFormatted = `<u>${authorsFormatted.split(', ')[0]}</u>${authorsFormatted.substring(authorsFormatted.indexOf(','))}`; // Underline the first author

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

        div.innerHTML = `
            <p>
                ${presentationList.length - index}. ${authorsFormatted} "${entry.title}". 
                <em>${entry.conference}</em>. ${entry.type}. ${entry.location}, ${entry.date}.
                ${links.length > 0 ? '<br>' + links : ''}
            </p>
        `;
        container.appendChild(div);
    });
}


    window.onload = function() {
        displayJournalList();
        displayPresentationList();
    };
</script>


### Preprint
<div id="preprint">
    <p>
        *<strong>S. Lee</strong>, C. Chen, G. Garcia, and A. O. Oliynyk, 
        Machine learning descriptors in materials chemistry: prediction and experimental validation synthesis of novel intermetallic UCd<sub>3</sub> (2023).
        <br>
        <a href="https://doi.org/10.26434/chemrxiv-2023-0nlzl">ChemRxiv</a>
    </p>
</div>

### Journals
<div id="journalList"></div>

### Book chapter
<div id="bookChapter">
    <p>
        1. R. Q. Topper, S. L. Topper, and <strong>S. Lee</strong>, 
        TransRot: A Portable Software Package for Simulated Annealing Monte Carlo Geometry Optimization of Atomic and Molecular Clusters
        in <em>ACS Symposium Series: Physical Chemistry Research at Undergraduate Institutions: Innovative and Impactful Approaches</em>, 
        Volume 1, C. A. Parish and T. A. Hopkins, Eds., ACS Publications, <strong>1428</strong>, 2, 19-38 (2022). <br><a href="https://doi.org/10.1021/bk-2022-1428.ch002">DOI</a> |
        <a href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=L07HlVsAAAAJ&authuser=1&citation_for_view=L07HlVsAAAAJ:d1gkVwhDpl0C">Google Scholar</a> 
    </p>
</div>

### Presentations
<div id="presentationList"></div>
