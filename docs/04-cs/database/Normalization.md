# Normalization

> 資料庫正規化的目的是消除資料冗餘、避免更新異常，讓資料結構更具一致性與可維護性


| StudentID | StudentName | Courses           | Instructors        |
|-----------|-------------|-------------------|--------------------|
| 001       | Alice       | Math, Physics     | Smith, Johnson     |
| 002       | Bob         | Chemistry         | Williams           |

## 1NF

欄位不可再分割

將每筆紀錄拆成一列，只包含單一課程與對應的老師
學生資訊組成學生資訊表，有年齡、性別、學號等資訊組成。這些欄位都不可再分

Splits multi-valued fields into separate rows

| StudentID | StudentName | Course    | Instructor |
|-----------|-------------|-----------|------------|
| 001       | Alice       | Math      | Smith      |
| 001       | Alice       | Physics   | Johnson    |
| 002       | Bob         | Chemistry | Williams   |

## 2NF

滿足第一正規化,表中的欄位必須完全依賴於全部主鍵而非部分主鍵
所有資料都要和該資料表的鍵（主鍵與候選鍵）有完全相依關係

StudentName 只與 StudentID 有關，不需重複出現在每筆選課紀錄中

Split StudentName into a separate table to remove partial dependency

#### Student Table
| StudentID | StudentName |
|-----------|-------------|
| 001       | Alice       |
| 002       | Bob         |

#### Enrollments Table (Still includes Instructor)
| StudentID | Course    | Instructor |
|-----------|-----------|------------|
| 001       | Math      | Smith      |
| 001       | Physics   | Johnson    |
| 002       | Chemistry | Williams   |

## 3NF

滿足第二正規化，非主鍵外的所有欄位必須互不依賴
消除傳遞相依（A → B → C）

Instructor 是依據 Course 決定的，而不是 StudentID

將課程與授課老師的對應關係也拆成獨立表格

remove transitive dependency: Instructor depends on Course, not Student.

#### Courses Table
| CourseID | CourseName | Instructor |
|----------|------------|------------|
| C001     | Math       | Smith      |
| C002     | Physics    | Johnson    |
| C003     | Chemistry  | Williams   |

#### Enrollments Table
| StudentID | CourseID |
|-----------|----------|
| 001       | C001     |
| 001       | C002     |
| 002       | C003     |
