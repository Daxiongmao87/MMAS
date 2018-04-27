import os
import sqlite3
from flask import Flask, render_template, request, g, \
        session, redirect, url_for, abort, flash

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'mmas.db'),
    SECRET_KEY='dev',
    USERNAME='admin',
    PASSWORD='admin'
    ))
app.config.from_envvar('MMAS_SETTINGS', silent=True)


sql_entries = ["select batting.player_id, max(batting.h), batting.ab, batting.team_id, batting.year from batting where batting.ab > 501 and batting.ab < 2000",
        "select batting.player_id, batting.h, batting.team_id, batting.year from batting where batting.h > 150 and batting.team_id = 'COL' and batting.year >= 1995 union select batting.player_id, batting.h, batting.team_id, batting.year from batting where batting.h > 150 and batting.team_id = 'SFN' and batting.year >= 1995 order by batting.h desc",
        "select pitching.player_id, pitching.r, pitching.er, pitching.era, pitching.h, pitching.hr, pitching.w, pitching.year, pitching.team_id from pitching where pitching.era <= 3.00 and pitching.year >= 1995 and pitching.gs >= 30 and pitching.team_id = 'COL' union select pitching.player_id, pitching.r, pitching.er, pitching.era, pitching.h, pitching.hr, pitching.w, pitching.year, pitching.team_id from pitching where pitching.era <= 3.00 and pitching.year >= 1995 and pitching.gs >= 30 and pitching.team_id = 'SFN' order by pitching.era asc",
        "select team.team_id, team.w, team.year from team where team.year >= 1995 and (team.team_id = 'COL' or team.team_id = 'SFN') order by team.w desc",
        "select batting.player_id, batting.hr, batting.team_id, batting.year from batting where batting.hr >= 30  and batting.year >= 1995 and (batting.team_id = 'KCA' or batting.team_id = 'BOS') order by batting.hr asc",
    
        "select fielding.player_id, fielding.team_id, fielding.g, fielding.year, fielding.pos, fielding.e, fielding.a from fielding where fielding.a >= 150 and fielding.e > 1 and fielding.year >= 1995 and fielding.g >= 100 and (fielding.team_id = 'NYA' or fielding.team_id = 'MIA') order by fielding.e desc",
        "select all_star.player_id, all_star.team_id, all_star.year, salary.salary from ((all_star inner join salary on all_star.player_id = salary.player_id)) where all_star.year >= 2010 and salary.salary > 20000000 order by salary.salary desc",
        "select all_star.player_id, all_star.team_id, all_star.year, salary.salary from ((all_star inner join salary on all_star.player_id = salary.player_id)) where all_star.year >= 2005 and salary.salary < 1000000 order by salary.salary asc",
        "select pitching.player_id, pitching.year, player_college.player_id, pitching.era, pitching.g from ((pitching inner join player_college on pitching.player_id = player_college.player_id)) where player_college.college_id = 'lsu' and pitching.era < 3.00 and pitching.g > 2 order by pitching.era asc",
        "select distinct pitching.player_id, pitching.era, pitching.r, pitching.er, pitching.w, pitching.gs, pitching.cg, pitching.hr, pitching.so, pitching.sho, pitching.bb, pitching.team_id, pitching.league_id, pitching.year, player_award.award_id from ((pitching inner join player_award on pitching.player_id = player_award.player_id)) where pitching.year >= 2010 and player_award.award_id = 'Cy Young Award' order by pitching.era asc"
        ]

entries_name = ["Since 1871, what qualified batter has had the most hits?",
        "Comparison of the number of hitters with more than 150 hits in a season based on two opposite home parks: Hitter-friendly Coor's Field(Colorado) and Pitcher-friendly AT&T Park (San Francisco).",
        "Comparison of pitching statistics based upon the players home park being either the most hitter friendly or the most pitcher friendly (in the NL), based on MLB's adjusted park factors.",
        "Query to find the number of wins by Colorado and San Francisco in each season since 1995 (When Coor's field opened). Does playing in a hitter-friendly or pitcher-friendly park have a large impact on total wins?",
        "Query of players with more than 30 home runs, filtered by American League and home field being Hitter Friendly or Pitcher Friendly - according to MLN's adjusted park factors.",
        "Query to determine whether or not fielding percentage is affected by playing for a northeastern team in an outdoor park(snow, rain, etc) versus playing for a southern team inside a dome.",
        "Query to search for all star players with a salary of more than $20 million. Are more expensive players always better?",
        "Query to find the number of all stars paid less than $1 million, which is generally going to be younger players offered the league minimum before they are eligible for artibration.",
        "Query to find the pitching statistics of former LSU baseball players, sorted by ERA",
        "Query to compare the statistics of Cy Young Award finalists and winners since 2010. Is there an easily-identifiable and direct correlation between any of the particular fields?"
        ]
@app.route("/")
def main():
    db = get_db()
    entries=[]
    entries_rows=[]
    entries_columns=[]
    entries_column_names=[]
    for i in range(0,len(sql_entries)):
        cur = db.execute(sql_entries[i])
        table=[]
        table_column_names=[]
        table.append(cur.fetchall())
        entries.append(table[0])
        row_count = 0;
        cur = db.execute(sql_entries[i])
        for row in cur:
          row_count += 1
          #print(table)
        entries_rows.append(row_count)
        cur = db.execute(sql_entries[i])
        column_count = 0;
        for row in cur.description:
          table_column_names.append(row[0])
          column_count += 1
        entries_column_names.append(table_column_names)
        entries_columns.append(column_count)
        #print('{0} , {1}'.format(entries_columns[i], entries_rows[i]))
    print('TOTAL: Row_index: {0} Column_index: {1}'.format(len(entries_columns), len(entries_rows)))
    return render_template(
            "index.html",
            entries=entries,
            entries_rows=entries_rows,
            entries_columns=entries_columns,
            entries_name=entries_name,
            entries_column_names=entries_column_names
            )

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    print(rv)
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Init database')

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

if __name__ == "__main__":
    app.run()
