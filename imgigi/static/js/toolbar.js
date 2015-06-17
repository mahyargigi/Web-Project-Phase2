/**
* Created by User on 5/3/15.
*/
$(document).ready(function(){
   $('#search').typeahead({
            name: 'accounts',
            local: ['Audi', 'BMW', 'Bugatti', 'Ferrari', 'Ford', 'Lamborghini', 'Mercedes Benz', 'Porsche', 'Rolls-Royce', 'Volkswagen']
        });
        var substringMatcher = function (strs) {
            return function findMatches(q, cb) {
                var matches, substringRegex;

                // an array that will be populated with substring matches
                matches = [];

                // regex used to determine if a string contains the substring `q`
                substrRegex = new RegExp(q, 'i');

                // iterate through the pool of strings and for any string that
                // contains the substring `q`, add it to the `matches` array
                $.each(strs, function (i, str) {
                    if (substrRegex.test(str)) {
                        matches.push(str);
                    }
                });

                cb(matches);
            };
        };

        var states = ['The Shawshank Redemption', 'The Godfather', 'The Godfather: Part II', 'The Dark Knight',
            'Pulp Fiction', "Schindler's List", '12 Angry Men', 'The Good, the Bad and the Ugly',
            'The Lord of the Rings: The Return of the King', 'Fight Club',
            'The Lord of the Rings: The Fellowship of the Ring', 'Star Wars: Episode V - The Empire Strikes Back',
            'Forrest Gump', 'Inception', "One Flew Over the Cuckoo's Nest", 'The Lord of the Rings: The Two Towers',
            'Goodfellas', 'The Matrix', 'Star Wars: Episode IV - A New Hope', 'Seven Samurai', 'City of God', 'Se7en',
            'The Usual Suspects', 'The Silence of the Lambs', 'Interstellar', "It's a Wonderful Life",
            'Léon: The Professional', 'Life Is Beautiful', 'Once Upon a Time in the West', 'Casablanca',
            'American History X', 'Saving Private Ryan', 'Raiders of the Lost Ark', 'Spirited Away', 'City Lights',
            'Psycho', 'Rear Window', 'Whiplash', 'The Intouchables', 'Modern Times', 'Terminator 2: Judgment Day',
            'The Green Mile', 'Memento', 'The Pianist', 'The Departed', 'Gladiator', 'Apocalypse Now', 'Sunset Blvd.',
            'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb', 'Back to the Future', 'Alien',
            'The Prestige', 'The Lion King', 'The Great Dictator', 'The Lives of Others', 'Cinema Paradiso',
            'Django Unchained', 'The Shining', 'The Dark Knight Rises', 'Paths of Glory', 'American Beauty',
            'WALL·E', 'North by Northwest', 'Aliens', 'Citizen Kane', 'Grave of the Fireflies', 'Vertigo', 'M',
            'Amélie', 'Oldboy', 'Das Boot', 'Princess Mononoke', 'Star Wars: Episode VI - Return of the Jedi',
            'Once Upon a Time in America', 'Toy Story 3', 'Reservoir Dogs', 'A Clockwork Orange', 'Braveheart',
            'Taxi Driver', 'Double Indemnity', 'Requiem for a Dream', 'Witness for the Prosecution',
            'To Kill a Mockingbird', 'Lawrence of Arabia', 'Eternal Sunshine of the Spotless Mind',
            'Full Metal Jacket', 'The Sting', "Singin' in the Rain", 'Bicycle Thieves', 'Amadeus',
            'Monty Python and the Holy Grail', 'Snatch.', '2001: A Space Odyssey', 'For a Few Dollars More',
            'Rashomon',
            'L.A. Confidential', 'The Kid', 'All About Eve', 'The Apartment', 'Inglourious Basterds'];


        $('#search .typeahead').typeahead({
                    hint: true,
                    highlight: false,
                    minLength: 1
                },
                {
                    name: 'states',
                    source: substringMatcher(states)
                });
});