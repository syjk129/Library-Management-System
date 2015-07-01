/*Create Table Statements*/

CREATE TABLE IF NOT EXISTS User (
    username VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL,
    PRIMARY KEY (username)
    );

CREATE TABLE IF NOT EXISTS Staff (
    username VARCHAR(30) NOT NULL,
    PRIMARY KEY (username),
    FOREIGN KEY (username) REFERENCES User(username)
        ON DELETE CASCADE    ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS Student_Faculty (
    username VARCHAR(30) NOT NULL,
    name VARCHAR(30) NOT NULL,
    email  VARCHAR(30),
    address VARCHAR(30),
    dob DATE,
    gender ENUM('M', 'F'),
    faculty ENUM('Y','N') DEFAULT 'N',
    debarred ENUM('Y','N') DEFAULT 'N',
    penalty FLOAT(6,2) DEFAULT 0,
    department VARCHAR(30),
    PRIMARY KEY (username),
    FOREIGN KEY (username) REFERENCES User(username)
        ON DELETE CASCADE    ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS Book (
    isbn VARCHAR(30) NOT NULL,
    title VARCHAR(60) NOT NULL,
    edition VARCHAR(30) ,
    publisher VARCHAR(30) ,
    place_of_publication VARCHAR(30),
    copyright_year INT,
is_book_on_reserve ENUM('Y','N') DEFAULT 'N',
shelf_num INT NOT NULL,
name VARCHAR(30) NOT NULL,
    PRIMARY KEY(isbn)
    );


CREATE TABLE IF NOT EXISTS Authors(
    isbn VARCHAR(30) NOT NULL,
    authors_name VARCHAR(30) NOT NULL,
    PRIMARY KEY(isbn,authors_name),
    FOREIGN KEY (isbn) REFERENCES Book(isbn)
        ON DELETE CASCADE    ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS BookCopy (
isbn VARCHAR(30) NOT NULL, 
    copy_num INT NOT NULL,
    is_on_hold ENUM('Y','N') DEFAULT 'N',
    is_checked_out ENUM('Y','N') DEFAULT 'N',
    is_damaged INT DEFAULT 0,
    future_requester VARCHAR(30),
    PRIMARY KEY(copy_num,isbn),
    FOREIGN KEY(isbn) REFERENCES Book(isbn)
        ON DELETE CASCADE    ON UPDATE CASCADE,
    CHECK (is_damaged >= 0 AND is_damage <= 1)
    );
CREATE TABLE IF NOT EXISTS Issues (
issue_id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(30) NOT NULL,
isbn VARCHAR(30) NOT NULL,
copy_num INT NOT NULL,
    date_of_issue DATE NOT NULL,
    extension_date DATE NOT NULL,
    return_date DATE NOT NULL,
    count_of_extensions int DEFAULT 0,
    PRIMARY KEY (issue_id),
    FOREIGN KEY (username) REFERENCES User(username)
        ON DELETE CASCADE    ON UPDATE CASCADE,
    FOREIGN KEY (copy_num) REFERENCES BookCopy(copy_num)
        ON DELETE CASCADE    ON UPDATE CASCADE,
    FOREIGN KEY (isbn) REFERENCES Book(isbn)
        ON DELETE CASCADE    ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS Floor (
    floor_num INT NOT NULL,
    num_of_assistants INT,
    num_of_copiers INT,
    PRIMARY KEY (floor_num)
    );

CREATE TABLE IF NOT EXISTS Shelf (
    shelf_num INT NOT NULL,
    aisle_num INT NOT NULL,
    floor_num INT NOT NULL,
    PRIMARY KEY (shelf_num),
    FOREIGN KEY(floor_num ) REFERENCES Floor(floor_num )
        ON DELETE CASCADE    ON UPDATE CASCADE

);

CREATE TABLE IF NOT EXISTS Subject (
    name VARCHAR(30) NOT NULL,
    num_of_journals INT,
    floor_num INT NOT NULL,
    PRIMARY KEY (name),
    FOREIGN KEY(floor_num ) REFERENCES Floor(floor_num )
        ON DELETE CASCADE    ON UPDATE CASCADE
);




CREATE TABLE IF NOT EXISTS Keywords(
    name VARCHAR(30) NOT NULL,
    keywords VARCHAR(30) NOT NULL,
    PRIMARY KEY (name, keywords),
    FOREIGN KEY(name) REFERENCES Subject(name)
        ON DELETE CASCADE    ON UPDATE CASCADE
);
